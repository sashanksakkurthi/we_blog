import { ArrowRightIcon } from "@chakra-ui/icons";
import {
  Box,
  Container,
  Flex,
  Input,
  InputGroup,
  InputRightElement,
  Stack,
} from "@chakra-ui/react";
import React from "react";
import Like from "./Components/Like";
import NewPost from "./Components/NewPost";
import Comment from "./Components/Comment";
import UserPost from "./Components/UserPost";

const Dashboard = () => {
  return (
    <Flex align={"center"} justify={"center"}>
      <Box w={"2xl"} h={"xl"} bg={"white"}>
        <Stack justify={"center"} p={"6"}>
          <NewPost />
          <Stack
            p={"3"}
            border={"1px"}
            borderColor={"gray.300"}
            borderRadius={"md"}
          >
            <UserPost />
            <Flex h={"10"} align={"center"}>
              <Like />
              <Comment />
            </Flex>
          </Stack>
        </Stack>
      </Box>
    </Flex>
  );
};

export default Dashboard;
