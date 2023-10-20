"use client";
import * as React from "react";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import { createTheme } from "@mui/material/styles";
import { SignUpProps } from "../../component/interfaces";
import Snackbar from "../../component/Snackbar";
import CircularProgress from "@mui/material/CircularProgress";

const defaultTheme = createTheme();

export default function MovieFormDialog({
  loading,
  showMessage,
  setShowMessage,
  message,
  messageColor,
  formHandleSubmit,
  onSubmit,
  register,
  errors,
}: SignUpProps) {

  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button className="text-black font-bold border-black mb-4" variant="outlined" onClick={handleClickOpen}>
        Add Movie
      </Button>
      <br></br>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Create Movie</DialogTitle>
        <DialogContent>
        <form noValidate>
          <TextField
            autoFocus
            required
            margin="dense"
            id="moviename"
            label="Movie Name"
            type="text"
            fullWidth
            {...register("moviename")}
            error={Boolean(errors?.moviename)}
            helperText={errors?.moviename ? errors?.moviename.message : " "}
          />
          <TextField
            autoFocus
            required
            margin="dense"
            id="year"
            label="Year"
            type="number"
            fullWidth
            {...register("year")}
            error={Boolean(errors?.year)}
            helperText={errors?.year ? errors?.year.message : " "}
          />
          <TextField
            autoFocus
            margin="dense"
            id="director"
            label="Director"
            type="text"
            fullWidth
            {...register("director")}
            error={Boolean(errors?.director)}
            helperText={errors?.director ? errors?.director.message : " "}
          />
          <TextField
            autoFocus
            margin="dense"
            id="description"
            label="Description"
            type="text"
            fullWidth
            {...register("description")}
            error={Boolean(errors?.description)}
            helperText={errors?.description ? errors?.description.message : " "}
          />
        </form>
        {message !== "" ? (
            <Snackbar
              showMessage={showMessage}
              setShowMessage={setShowMessage}
              message={message}
              messageColor={messageColor}
            />
          ) : null}
          {loading ? (
            <Box>
              <CircularProgress />
            </Box>
          ) : null}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button
              type="submit"
              onClick={() => {
                formHandleSubmit(onSubmit)();
                handleClose();
              }}
            >
              Submit
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
