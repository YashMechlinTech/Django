import React, { useState } from "react";
import { useMutation, gql } from "@apollo/client";

const CREATE_TODO = gql`
  mutation CreateTodo($title: String!, $description: String) {
    createTodo(title: $title, description: $description) {
      todo {
        id
        title
        description
        completed
    
      }
    }
  }
`;

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


const AddTodo = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [createTodo, { loading, error }] = useMutation(CREATE_TODO, {
    refetchQueries: [{ query: GET_TODOS }],
  });
  const handleSubmit=async(e)=>{
    e.preventDefault();
    if(!title) return ;
    await createTodo({variables:{title,description}})
    setTitle('')
    setDescription('')
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="todo Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      

      <button type="submit" disabled={loading}>
        Create Task
      </button>
      {error && <p>Error adding todo. </p>}
    </form>
  );
};

export default AddTodo;
