import glob, os, re, subprocess

d='..'
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))];
folders.sort()
for folder in folders:
    for filename in glob.glob(folder+'/*.frag'):
        # print filename
        shaderPath = filename;
        shaderName,shaderExt = os.path.splitext(filename)
        shaderImage = shaderName+".png"
        shaderCommand = "glslViewer " + shaderPath + " " + \
                            " -s 0.5 -o " + shaderImage
        returnCode = subprocess.call(shaderCommand, shell=True)
