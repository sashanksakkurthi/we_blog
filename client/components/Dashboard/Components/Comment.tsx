import {
  Avatar,
  Text,
  HStack,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalHeader,
  ModalOverlay,
  Stack,
  Button,
  useDisclosure,
} from "@chakra-ui/react";
import React from "react";

const Comment = () => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <div>
      <Button
        bg={"white"}
        aria-label={""}
        size={"sm"}
        fontFamily={"Roboto"}
        textColor={"gray.600"}
        _hover={{ bg: "white" }}
        onClick={onOpen}
        leftIcon={
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="#0ea5e9"
            viewBox="0 0 16 16"
          >
            <path d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H4.414A2 2 0 0 0 3 11.586l-2 2V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12.793a.5.5 0 0 0 .854.353l2.853-2.853A1 1 0 0 1 4.414 12H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
            <path d="M5 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z" />
          </svg>
        }
      >
        0
      </Button>
      <Modal onClose={onClose} isOpen={isOpen} isCentered>
        <ModalOverlay />
        <ModalContent minH={"72"} overflowY={"scroll"}>
          <ModalCloseButton />
          <ModalBody pt={"10"}>
            <Stack>
              <Input
                placeholder={"Make a Comment"}
                size={"sm"}
                rounded={"md"}
              />
              <Stack
                border={"1px"}
                rounded={"md"}
                borderColor={"gray.300"}
                p={"2"}
              >
                <HStack>
                  <Avatar size={"xs"} />
                  <Text
                    fontFamily={"Inter"}
                    fontSize={"x-small"}
                    fontWeight={"medium"}
                  >
                    Sakkurthi Sashank
                  </Text>
                </HStack>
                <Text
                  fontWeight={"normal"}
                  fontSize={"small"}
                  fontFamily={"Roboto"}
                >
                  Hey its good to see you
                </Text>
              </Stack>
            </Stack>
          </ModalBody>
        </ModalContent>
      </Modal>
    </div>
  );
};

export default Comment;
