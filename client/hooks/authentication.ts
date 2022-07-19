import Cookies from "universal-cookie";
import axios from "axios";
import { useState, useEffect } from "react";

const cookies = new Cookies();
const token = cookies.get("access_token");

const urls = `${process.env.NEXT_PUBLIC_BACKEND_URL}/verify/`;

const Authentication = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  useEffect(() => {
    const isAuthenticated = async () => {
      await axios
        .post(
          urls,
          {},
          {
            headers: {
              Authorization: token.access_token,
            },
          }
        )
        .then((response) => {
          if (response.status === 202) {
            setIsAuthenticated(true);
            setEmail(response.data.email);
            setName(response.data.name);
          } else {
            setIsAuthenticated(false);
          }
        });
    };
    isAuthenticated();
  }, []);
  return { isAuthenticated, name, email };
};

export default Authentication;
