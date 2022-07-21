import { Button, Input, InputGroup } from "@chakra-ui/react";
import React from "react";
import Authentication from "../../../hooks/authentication";

const NewPost = () => {
  
  const authentication = Authentication();

  const urls = `${process.env.NEXT_PUBLIC_BACKEND_URL}/create-post/`;

  const [postValue, setPostValue] = React.useState();

  const HandleInputChange = (event: any) => {
    setPostValue(event.target.value);
  };

  const HandleInputSubmit = async () => {
    const response = await fetch(urls, {
      method: "POST",
      body: JSON.stringify({
        content: postValue,
      }),
      headers: {
        "Content-type": "application/json",
        Authorization: authentication.token,
      },
    });
    const data = await response.json();
  };

  return (
    <InputGroup alignItems={"center"}>
      <Input
        isRequired
        placeholder="Start a Post"
        fontFamily={"Roboto"}
        borderColor={"gray.400"}
        onInput={HandleInputChange}
        _placeholder={{
          fontFamily: "Roboto",
          textColor: "gray.600",
        }}
        size="md"
      />
      <Button
        size={"sm"}
        border={"1px"}
        borderColor={"gray.300"}
        py={"4"}
        ml={"1"}
        bg={"white"}
        fontFamily={"Inter"}
        fontSize={"sm"}
        _hover={{
          bg: "white",
        }}
        textColor={"gray.700"}
        onClick={HandleInputSubmit}
      >
        Post
      </Button>
    </InputGroup>
  );
};

export default NewPost;
