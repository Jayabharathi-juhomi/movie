import * as React from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";
import { MoviesProps } from '@/app/component/interfaces';

export default function MovieList({
  movies
}: MoviesProps) {
  return (
    <Box sx={{ width: '200%',height: '200%' }}>
      <Grid container spacing={1} sx={{ alignItems: "center" }}>
        {movies.map((movie: any) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={movie.id}>
            <Paper elevation={3} sx={{ padding: 2, width: '100%', height: '100%' }}>
              <Box
                sx={{
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  width: '100%',
                  height: '100%',
                  alignItems: "center",
                }}
              >
                <Typography variant="h6" gutterBottom>{movie.title}</Typography>
                <Typography>{movie.year}</Typography>
                <Typography>{movie.director}</Typography>
                <Typography>{movie.description}</Typography>
              </Box>
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}