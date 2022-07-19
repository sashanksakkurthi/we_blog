import Cookies from "universal-cookie";
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
      const response = await fetch(urls, {
        method: "POST",
        headers: {
          Authorization: token,
        },
      });
      const data = await response.json();
      if (response.status === 202) {
        setIsAuthenticated(true);
        setEmail(data.email);
        setName(data.name);
      } else {
        setIsAuthenticated(false);
      }
    };
    isAuthenticated();
  }, []);
  return { isAuthenticated, name, email };
};

export default Authentication;
