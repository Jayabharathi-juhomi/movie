import { MovieFormData } from "../../component/interfaces";

export async function createMovie(formData: MovieFormData) {
    const body = {
      title: formData.moviename, year: formData.year, 
      description: formData.description, director: formData.director
    };
    const res = await fetch("http://127.0.0.1:8000/api/v1/movies", {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify(body),
    });
    return res;
  }

  export async function movieList() {
    const res = await fetch("http://127.0.0.1:8000/api/v1/movies", {
      method: "GET",
      headers: { "Content-type": "application/json" },
    });
    return res;
  }