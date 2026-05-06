from PIL import Image
from torchvision import transforms
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
import numpy as np


device = "cuda" if torch.cuda.is_available() else "cpu"

model_path = "/share/home/zymatrix/NeuroClips/blip2"
processor = Blip2Processor.from_pretrained(model_path, local_files_only=True)
model = Blip2ForConditionalGeneration.from_pretrained(model_path, local_files_only=True, torch_dtype=torch.float16)
model.to(device)


images = torch.load('/share/home/zymatrix/NeuroClips/cc2017/GT_test_3fps.pt',map_location='cpu')[:,2,:,:,:]
print(images.shape)
all_predcaptions = []
for i in range(images.shape[0]):
    x = images[i]
    x = transforms.ToPILImage()(x)
    inputs = processor(images=x, return_tensors="pt").to(device, torch.float16)

    generated_ids = model.generate(**inputs)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    all_predcaptions = np.hstack((all_predcaptions, generated_text))
    print(generated_text, all_predcaptions.shape)

torch.save(all_predcaptions, f'/share/home/zymatrix/NeuroClips/cc2017/GT_test_caption.pt')


images = torch.load('/share/home/zymatrix/NeuroClips/cc2017/GT_train_3fps.pt',map_location='cpu')[:,2,:,:,:]
print(images.shape)
all_predcaptions = []
for i in range(images.shape[0]):
    x = images[i]
    x = transforms.ToPILImage()(x)
    inputs = processor(images=x, return_tensors="pt").to(device, torch.float16)

    generated_ids = model.generate(**inputs)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    all_predcaptions = np.hstack((all_predcaptions, generated_text))
    print(generated_text, all_predcaptions.shape)

torch.save(all_predcaptions, f'/share/home/zymatrix/NeuroClips/cc2017/GT_train_caption.pt')