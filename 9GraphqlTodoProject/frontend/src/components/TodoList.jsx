import React, { useState } from "react";
import { useQuery, gql, useMutation } from "@apollo/client";

const GET_TODOS = gql`
  query GetTodos {
    allTodos {
      id
      title
      description
      completed
    }
  }
`;

const TOGGLE_TODO = gql`
  mutation UpdateTodoStatus($id: ID!, $completed: Boolean!) {
    updateTodo(id: $id, completed: $completed) {
      todo {
        id
        completed
      }
    }
  }
`;

const DELETE_TODO = gql`
  mutation DeleteTodo($id: ID!) {
    deleteTodo(id: $id) {
      ok
    }
  }
`;

const UPDATE_TODO = gql`
  mutation UpdateTodoContent($id: ID!, $title: String!, $description: String!) {
    updateTodo(id: $id, title: $title, description: $description) {
      todo {
        id
        title
        description
      }
    }
  }
`;

const TodoList = () => {
  const { loading, error, data, refetch } = useQuery(GET_TODOS);
  const [toggleTodo] = useMutation(TOGGLE_TODO);
  const [deleteTodo] = useMutation(DELETE_TODO);
  const [updateTodo] = useMutation(UPDATE_TODO);

  const [editingTodo, setEditingTodo] = useState(null); // Track which todo is being edited
  const [editTitle, setEditTitle] = useState("");
  const [editDescription, setEditDescription] = useState("");

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error fetching todos.</p>;

  const handleToggle = async (id, currentStatus) => {
    await toggleTodo({
      variables: { id, completed: !currentStatus },
    });
    refetch();
  };

  const handleDelete = async (id) => {
    await deleteTodo({
      variables: { id },
    });
    refetch();
  };

  const handleEditClick = (todo) => {
    setEditingTodo(todo.id);
    setEditTitle(todo.title);
    setEditDescription(todo.description);
  };

  const handleUpdate = async (id) => {
    await updateTodo({
      variables: {
        id,
        title: editTitle,
        description: editDescription,
      },
    });
    setEditingTodo(null); // Exit editing mode
    refetch();
  };

  return (
    <ul>
      {data.allTodos.map((todo) => (
        <li key={todo.id} style={{ marginBottom: "10px" }}>
          <input
            type="checkbox"
            checked={todo.completed}
            onChange={() => handleToggle(todo.id, todo.completed)}
          />

          {editingTodo === todo.id ? (
            <div>
              <input
                type="text"
                value={editTitle}
                onChange={(e) => setEditTitle(e.target.value)}
                placeholder="Edit title"
              />
              <input
                type="text"
                value={editDescription}
                onChange={(e) => setEditDescription(e.target.value)}
                placeholder="Edit description"
              />
              <button onClick={() => handleUpdate(todo.id)}>Save</button>
              <button onClick={() => setEditingTodo(null)}>Cancel</button>
            </div>
          ) : (
            <div>
              <strong
                style={{
                  textDecoration: todo.completed ? "line-through" : "none",
                }}
              >
                {todo.title}
              </strong>
              <p>{todo.description}</p>
           <div >
           <button style={{marginRight:'10px',backgroundColor:'steelblue'}} onClick={() => handleEditClick(todo)}>Edit</button>
           <button style={{backgroundColor:'crimson'}} onClick={() => handleDelete(todo.id)}>Delete</button>
           </div>
            </div>
          )}
        </li>
      ))}
    </ul>
  );
};

export default TodoList;
