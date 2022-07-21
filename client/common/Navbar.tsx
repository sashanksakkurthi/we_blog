import { Box, Flex, Text } from "@chakra-ui/react";
import React from "react";

const Navbar = () => {
  return (
    <Box minW={"100hv"} bg={"gray.800"}>
      <Flex
        align={"center"}
        h={"16"}
        justify={{ base: "space-between", lg: "space-evenly" }}
        px={"6"}
      >
        <Box>
          <Text
            fontSize={"xl"}
            textColor={"white"}
            fontFamily={"Inter"}
            fontWeight={"semibold"}
          >
            Community Post
          </Text>
        </Box>
        <Flex>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            fill="white"
            viewBox="0 0 16 16"
          >
            <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z" />
          </svg>
        </Flex>
      </Flex>
    </Box>
  );
};

export default Navbar;
