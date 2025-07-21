import sys
from Methods.ScoreAGC import ScoreAGC 
import torch 
import torch.utils.model_zoo as model_zoo
import Methods.AGCAM.ViT_for_AGCAM as ViT_Ours
import numpy as np
import random

def set_seed(seed):
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
set_seed(777)

def create_vit_model(model_name, num_classes, state_dict, strict=True):
    model = ViT_Ours.create_model(model_name, pretrained=True, num_classes=num_classes).to('cuda')
    model.load_state_dict(state_dict if isinstance(state_dict, dict) else state_dict['model_state'], strict=strict)
    return model.eval()

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--input_img":
        img_path = sys.argv[2]
        state_dict = model_zoo.load_url("https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-vitjx/jx_vit_base_p16_224-80ecf9dd.pth", progress=True, map_location='cuda')
        model = create_vit_model("vit_base_patch16_224", 1000, state_dict)
        method = ScoreAGC(model)
        prediction, saliency_map = method(img_path)
        mask = torch.nn.Upsample(224, mode='bilinear', align_corners=False)(
            saliency_map.reshape(1, 1, 14, 14)
        )
        mask = normalize_mask(mask)
    else:
        print("Invalid Input Parameters")
        
    