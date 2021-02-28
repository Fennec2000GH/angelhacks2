import { Box, HStack, useRadio, useRadioGroup } from "@chakra-ui/react";
import React from 'react';

function CustomRadio(props) {
  const { getInputProps, getCheckboxProps } = useRadio(props)

  const input = getInputProps()
  const checkbox = getCheckboxProps()

  return (
    <Box as="label">
      <input {...input} />
      <Box
        {...checkbox}
        cursor="pointer"
        borderWidth="1px"
        _checked={{
          color: "white",
          bg: "gray"
        }}
        _focus={{
          boxShadow: "outline",
        }}
        px={5}
        py={3}
      >
        {props.children}
      </Box>
    </Box>
  )
}

function AlgorithmsRadioCard(props) {
  const algorithmsOptions = props.algorithms;

  const { getRootProps, getRadioProps } = useRadioGroup({
    name: "Algorithm to use",
    defaultValue: props.defaultValue,
    onChange: props.onChange,
  })

  const group = getRootProps()

  return (
    <HStack {...group}>
      {algorithmsOptions.map((value) => {
        const radio = getRadioProps({ value })
        return (
          <CustomRadio key={value} {...radio}>
            {value}
          </CustomRadio>
        )
      })}
    </HStack>
  )
}

export default AlgorithmsRadioCard;
