export interface SnackbarProps {
  showMessage: boolean;
  setShowMessage: any;
  message: string;
  messageColor: string;
}

export interface FormData {
  email: string;
  password: string;
  passwordConfirm: string;
}

export interface SignUpProps {
  loading: boolean;
  showMessage: boolean;
  setShowMessage: any;
  message: string;
  messageColor: string;
  onSubmit: any;
  formHandleSubmit: any;
  register: any;
  errors: any;
}

export interface SignInProps {
  loading: boolean;
  showMessage: boolean;
  setShowMessage: any;
  message: string;
  messageColor: string;
  onSubmit: any;
  formHandleSubmit: any;
  handleOauth: any;
  register: any;
  errors: any;
}

export interface MovieFormData {
  moviename: string;
  year: string;
  director: string;
  description: string;
}

export interface MoviesProps {
  movies: any;
}