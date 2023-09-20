"use client";
import * as yup from "yup";
import * as Constants from "../utils/constant";

const schema = yup.object().shape({
    moviename: yup
        .string()
        .required(Constants.MOVIENAME_REQUIRED),
    year: yup
        .string()
        .required(Constants.YEAR_REQUIRED),
    director: yup
        .string(),
    description: yup
        .string()
});

export default schema;