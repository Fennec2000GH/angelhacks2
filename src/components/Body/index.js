
import { Button, Flex, Text, Textarea, VStack } from "@chakra-ui/react";
import React from 'react';

export default function Body() {
  //first text box
  let [value, setValue] = React.useState("")

  let handleInputChange = (e) => {
    let inputValue = e.target.value
    setValue(inputValue)
  }

  let [outputValue, setOutputValue] = React.useState("");

  function handleClick() {
    return () => {
      fetch('/data', {
        method: 'POST',
        headers: { "Content-type": "application/json; charset=UTF-8" },
        mode: 'cors',
        body: JSON.stringify(value)
      })
      .then((response) => {
        return response.json().then((data) => {
          console.log(data); //for debugging
          setOutputValue(data);
          return data;
        }).catch((err) => {
          console.log(err);
        });
      });
    };
  }

  return (
    <Flex
      minH={"50vh"}
      justify={"center"}
      w="100%"
    >
      <VStack
        spacing={10}
        w="100%"
        maxW="960px"
        px="2rem"
      >
        <Text>Enter text below so we can summarize it for you</Text>
        <Textarea
          size={"lg"}
          placeholder={"Lorem ipsum"}
          onChange={handleInputChange}
          value={value}
        >
        </Textarea>
        <Button
          onClick={handleClick()}
        >Summarify it</Button>
        <Textarea
          size={"lg"}
          readOnly={true}
          placeholder={"Lorem ipsum"}
          value={outputValue}
        ></Textarea>
      </VStack>
    </Flex>
  );
}
