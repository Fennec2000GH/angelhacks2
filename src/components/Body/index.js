import { Button, Flex, Spacer, Text, Textarea, VStack } from "@chakra-ui/react";
import React from 'react';
import AlgorithmsRadioCard from './AlgorithmsRadioCard'

export default function Body() {
  const algorithms = ["LexRank", "Luhn", "LSA", "KL"];
  let [textToSummarize, setTextToSummarize] = React.useState("")
  let [outputValue, setOutputValue] = React.useState("");
  let [algorithm, setAlgorithm] = React.useState(algorithms[0]);

  let handleInputChange = (e) => {
    let inputValue = e.target.value
    setTextToSummarize(inputValue)
  }

  const handleClick = (e) => {
    e.preventDefault();
    fetch('/data', {
      method: 'POST',
      headers: { "Content-type": "application/json; charset=UTF-8" },
      mode: 'cors',
      body: JSON.stringify(textToSummarize)
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
  }

  const handleAlgorithmsChange = (value) => {
    setAlgorithm(value);
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
          value={textToSummarize}
        >
        </Textarea>
        <Text>Select the algorithm to use:</Text>
        <AlgorithmsRadioCard
          algorithms={algorithms}
          defaultValue={algorithm}
          onChange={handleAlgorithmsChange}
        />
        <Spacer minH=".5rem" maxH="1rem" />
        <Button onClick={handleClick}>Summarify it</Button>
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
