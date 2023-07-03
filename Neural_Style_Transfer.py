import torch
import torch.nn as nn
import torch.optim as optim
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
from torchvision.utils import save_image


class VGG(nn.Module):

    def __init__(self):

        super(VGG, self).__init__()

        self.chosen_features= ['0','5','10','19','28']
        self.model= models.vgg19(pretrained= True).features[:29]

    def forward(self, x):

        features= []
        for layer_no, layer in enumerate(self.model):
            x= layer(x)
            if str(layer_no) in self.chosen_features:
                features.append(x)

        return features


def load_image(image_name):

    image= Image.open(image_name)
    image= loader(image).unsqueeze(0)

    return image.to(device)


device= torch.device("cuda")
model= VGG().to(device).eval()
image_size= 960


loader= transforms.Compose(
[
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean= [0.485, 0.456, 0.406], std= [0.229, 0.224, 0.225])

])


original_img= load_image('/kaggle/input/outputtesting/input4.jpg')
style_img= load_image('/kaggle/input/outputtesting/style4.jpg')
gen_img= original_img.clone().requires_grad_(True)


total_steps= 5001
learning_rate= 0.001
alpha= 1
beta= 0.1
optimizer= optim.Adam([gen_img], lr= learning_rate)


for step in range(total_steps):
    gen_features= model(gen_img)
    org_img_features= model(original_img)
    style_features= model(style_img)

    style_loss= content_loss=0
    #g= generated_image_feature
    #o= original_image_feature
    #s= style_image_feature
    for g, o, s in zip(gen_features, org_img_features, style_features):

        b_s, c, h, w= g.shape
        content_loss= content_loss+ torch.mean((g- o)**2)

        g_matrix= g.view(c, h*w).mm(g.view(c, h*w).t())
        a_matrix= s.view(c, h*w).mm(s.view(c, h*w).t())

        style_loss= style_loss + torch.mean((g_matrix- a_matrix)**2)
        total_loss= alpha*content_loss+ beta*style_loss

        optimizer.zero_grad()
        total_loss.backward(retain_graph=True)
        optimizer.step()

        if step%200==0:
            denorm= transforms.Normalize((-2.12, -2.04, -1.80), (4.37, 4.46, 4.44))
            img = gen_img.clone().squeeze()
            img = denorm(img).clamp_(0, 1)
            save_image(img, "generated_{}.png".format(step))

