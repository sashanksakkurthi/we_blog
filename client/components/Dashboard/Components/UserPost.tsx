import { Avatar, Box, Divider, HStack, Text } from "@chakra-ui/react";
import React from "react";

const UserPost = () => {
  return (
    <div>
      <HStack pb={"2"} borderBottom={"1px"} borderColor={"gray.300"}>
        <Avatar size={"sm"} />
        <Box>
          <Text fontFamily={"Inter"} fontSize={"sm"} fontWeight={"medium"}>
            Sakkurthi Sashank
          </Text>
          <Text fontFamily={"Inter"} fontSize={"x-small"} fontWeight={"normal"}>
            Posted at 20/7/2022
          </Text>
        </Box>
      </HStack>

      <Text
        fontWeight={"normal"}
        pt={"3"}
        pl={"6"}
        fontSize={"sm"}
        fontFamily={"Roboto"}
      >
        Hey
      </Text>
    </div>
  );
};

export default UserPost;
