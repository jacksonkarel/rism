import replicate


def codellama_generate(prompt):
    codellama_model_version = "meta/codellama-34b:efbd2ef6feefb242f359030fa6fe08ce32bfced18f3868b2915db41d41251b46"
    output = replicate.run(
        codellama_model_version,
        input={
            "prompt": prompt,
            "max_tokens": 5000,
        },
    )
    output_str = "".join(output)
    print("Codellama:\n", output_str)

    return output_str
