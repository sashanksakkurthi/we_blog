import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  Stack,
  Button,
  Heading,
  useColorModeValue,
} from "@chakra-ui/react";
import { useState } from "react";
import Cookies from "universal-cookie";
import { useRouter } from "next/router";

const cookies = new Cookies();

export default function SignIn() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const HandleEmailInput = (event: any) => {
    setEmail(event.target.value);
  };
  const HandlePasswordInput = (event: any) => {
    setPassword(event.target.value);
  };

  const urls = `${process.env.NEXT_PUBLIC_BACKEND_URL}/login/`;

  const handleLogin = async (event: any) => {
    const form_data = new FormData();
    cookies.remove("access_token");

    form_data.append("username", email);
    form_data.append("password", password);

    const response = await fetch(urls, {
      method: "POST",
      body: form_data,
    });
    const data = await response.json();
    if (response.status === 200) {
      cookies.set("access_token", data.access_token, {
        path: "/",
      });
      router.push("/");
    }
  };

  return (
    <Flex minH={"100vh"} align={"center"} justify={"center"} bg={"gray.50"}>
      <Stack spacing={8} mx={"auto"} maxW={"lg"} py={12} px={6}>
        <Heading fontSize={"2xl"} textAlign={"center"} fontFamily={"Roboto"}>
          Sign in to your account
        </Heading>
        <Box
          rounded={"lg"}
          bg={useColorModeValue("white", "gray.700")}
          boxShadow={"lg"}
          p={8}
        >
          <Stack spacing={4} width={{ base: "64", sm: "80" }}>
            <FormControl id="email">
              <FormLabel
                textColor={"#1f2937"}
                fontFamily={"Inter"}
                fontSize={"sm"}
                fontWeight={"bold"}
              >
                Email address
              </FormLabel>
              <Input
                type="email"
                placeholder="Enter your email"
                _placeholder={{
                  fontFamily: "Inter",
                  opacity: 1,
                  color: "gray.500",
                  fontWeight: "regular",
                }}
                onInput={HandleEmailInput}
              />
            </FormControl>
            <FormControl id="password">
              <FormLabel
                textColor={"#1f2937"}
                fontFamily={"Inter"}
                fontSize={"sm"}
                fontWeight={"bold"}
              >
                Password
              </FormLabel>
              <Input
                type="password"
                placeholder="Enter password"
                _placeholder={{
                  fontFamily: "Inter",
                  opacity: 1,
                  color: "gray.500",
                  fontWeight: "regular",
                }}
                onInput={HandlePasswordInput}
              />
            </FormControl>
            <Button
              bg={"blue.400"}
              color={"white"}
              _hover={{
                bg: "blue.500",
              }}
              onClick={handleLogin}
            >
              Sign in
            </Button>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
}
