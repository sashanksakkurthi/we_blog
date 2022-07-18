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
import axios from "axios";
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

  const handleLogin = async (event: any) => {
    event?.preventDefault();
    cookies.remove("access_token");
    try {
      await axios
        .post(`${process.env.BACKEND_URL}/login`, {
          username: email,
          password: password,
        })
        .then((response: { data: { status: string } }) => {
          if (response.data.status !== "error") {
            cookies.set("access_token", response.data, { path: "/" });
            router.push("/");
          } else {
            router.push("/auth/login");
          }
        });
    } catch (error) {
      router.push("/auth/login");
      alert("Please check your username and password");
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
