import { Box } from "@chakra-ui/react";
import type { NextPage } from "next";
import Navbar from "../common/Navbar";
import Dashboard from "../components/Dashboard";

const Home: NextPage = () => {
  return (
    <>
      <Box bg={"gray.100"}>
        <Navbar />
        <Dashboard />
      </Box>
    </>
  );
};

export default Home;
