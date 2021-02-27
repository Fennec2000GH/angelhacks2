import { Button, Flex, Text, Textarea, VStack } from "@chakra-ui/react";
import React from 'react';

export default function Body() {
    let [value, setValue] = React.useState("")

    let handleInputChange = (e) => {
      let inputValue = e.target.value
      setValue(inputValue)
    }
    
    return (
        <Flex
            w="100vw"
            minH={"50vh"}
            justify={"center"}
        >
            <VStack
                spacing={10}
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
                    onClick={() => {
                        fetch('/data', {
                            method: 'POST', 
                            mode: 'cors',
                            body: JSON.stringify(value)})  
                        }}
                >Big Red Button</Button>
                <Textarea
                    size={"lg"}
                    placeholder={"Lorem ipsum"}
                ></Textarea>
            </VStack>
        </Flex>
    );
}