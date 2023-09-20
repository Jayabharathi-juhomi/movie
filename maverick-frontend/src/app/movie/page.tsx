"use client";
import React from "react";
import MovieForm from "./component/MovieForm";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import MovieList from "./component/MovieList";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Constants from "../utils/constant";
import registerSchema from "./validation";
import { useForm } from "react-hook-form";
import { createMovie, movieList } from "./api/route";
import { useRouter } from "next/navigation";
import { MovieFormData } from "./../component/interfaces";
import { useEffect } from 'react';

const defaultTheme = createTheme();

const Movie = () => {
  const [loading, setLoading] = React.useState(false);
  const [showMessage, setShowMessage] = React.useState(false);
  const [message, setMessage] = React.useState("");
  const [messageColor, setMessageColor] = React.useState(Constants.INFO);
  const [movies, setMovies] = React.useState([]);
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(registerSchema),
  });
  const router = useRouter();

  useEffect(() => {
    setLoading(true);
    const response = movieList()
      .then(async (res) => {
        const response = await res.json();
        console.log("response", response)
        if (res.status === 200) {
          setMovies(response);
        }
         setLoading(false);
      })
      .catch((error) => {
        setLoading(false);
      });
  })

  const submit = async (data: MovieFormData) => {
    setShowMessage(true);
    setLoading(true);
    const response = await createMovie(data)
      .then(async (res) => {
        const response = await res.json();
        if (res.status === 201) {
          setMessage(Constants.MOVIE_CREATED_SUCCESSFULLY);
          setMessageColor(Constants.SUCCESS);
        } else {
          const data = response.detail;
          setMessage(data);
          setMessageColor(Constants.ERROR);
        }
         setLoading(false);
      })
      .catch((error) => {
        setMessage(error);
        setLoading(false);
        setMessageColor(Constants.ERROR);
      });
  };

  return(
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
      <MovieForm
        loading={loading}
        showMessage={showMessage}
        setShowMessage={setShowMessage}
        message={message}
        messageColor={messageColor}
        onSubmit={submit}
        formHandleSubmit={handleSubmit}
        register={register}
        errors={errors}
        />
      <MovieList
      movies={movies}
      />
    </Box>
  </Container>
  </ThemeProvider>
  );
};
export default Movie;

  