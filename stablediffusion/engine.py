from diffusers import DiffusionPipeline
from diffusers import DPMSolverMultistepScheduler
from pathlib import Path
import torch


BASE_DIR = Path(__file__).resolve().parent.parent
sd_dir = BASE_DIR / 'stablediffusion/sd_models/sd1-5'


class TestEngine:
	def __init__(self, prompt):
		self.prompt = prompt

	def test_diffusion_pipeline(self):
		pipeline = DiffusionPipeline.from_pretrained(sd_dir, torch_dtype=torch.float16)
		pipeline = pipeline.to("cuda")
		pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)
		generator = torch.Generator("cuda").manual_seed(0)
		image = pipeline(self.prompt, generator=generator, num_inference_steps=20).images[0]

		return image
