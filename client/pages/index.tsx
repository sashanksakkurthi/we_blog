import type { NextPage } from "next";
import Authentication from "../hooks/authentication";

const Home: NextPage = () => {
  const authentication = Authentication();
  return (
    <>
      {authentication.isAuthenticated ? (
        <div>
          {authentication.email} <br /> {authentication.name}
        </div>
      ) : (
        <div>Not authenticated</div>
      )}
    </>
  );
};

export default Home;
