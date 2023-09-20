import * as React from 'react';
import Grid from '@mui/material/Unstable_Grid2';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";
import { MoviesProps } from '@/app/component/interfaces';

export default function Movielist({
  movies
}: MoviesProps
) {
  return (

    <Box sx={{ width: '100%' }}>
      <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
        <Grid xs={6}>
          {movies.map((movie: any) =>

        <Box
        sx={{
        display: 'flex',
        flexWrap: 'wrap',
        flexDirection: "row",
        '& > :not(style)': {
          m: 1,
          width: 150,
          height: 150,
        },
      }}
    >

      <Paper elevation={3}>
        <Box
        sx={{
            marginTop: 1,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
        }}
        >
        <Typography variant="h6" gutterBottom>{movie.title}</Typography>
        <Typography>{movie.year}</Typography>
        <Typography>{movie.director}</Typography>
        <Typography>{movie.description}</Typography>
        </Box>

      </Paper>
    </Box>
    )}
        </Grid>
      </Grid>
    </Box>
  );
}