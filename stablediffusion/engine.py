from diffusers import DiffusionPipeline, EulerDiscreteScheduler


class TestEngine:
	def __init__(self, prompt):
		self.prompt = prompt

	def test_diffusion_pipeline(self):
		pipeline = DiffusionPipeline.from_pretrained("./sd_models/stable-diffusion-v1-5", use_safetensors=True)
		pipeline.scheduler = EulerDiscreteScheduler.from_config(pipeline.scheduler.config)
		pipeline.to("cuda")
		image = pipeline(self.prompt).images[0]

		return image
