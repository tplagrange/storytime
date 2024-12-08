import torch
from diffusers import EulerDiscreteScheduler, StableDiffusionPipeline

model_id = "stabilityai/stable-diffusion-2-1"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, torch_dtype=torch.float16
)  # to("cuda")
device = "mps" if torch.backends.mps.is_available() else "cpu"
pipe = pipe.to(device)
_ = pipe("test", num_inference_steps=1, height=384, width=384)


def illustrate_from_prompt(prompt):
    # Generate an image from the prompt
    image = pipe(
        prompt,
        height=512,  # smaller resolution
        width=512,
    ).images[0]
    return image
