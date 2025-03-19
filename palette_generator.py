def palette_generator(colours=['#139FBE', '#054655', '#0E788F'], size=(8, 1), with_saturation={}):
    try:
        from matplotlib import pyplot as plt 
        from matplotlib import patches 
    except(ModuleNotFoundError):
        return 'ModuleNotFound: The matplotlib library was not found.'
    
    for i in with_saturation.values():
         if i < 0 or i > 1:
              raise ValueError('Saturation values should be in the range 0-1.')

    fig, ax = plt.subplots(figsize=size) 
    for i, colour in enumerate(colours):
        if colour in with_saturation.keys():
                ax.add_patch(patches.Rectangle((i, 0), 1, 1, color=colour, alpha=with_saturation.get(colour))) # the first value defines the x, y position of the Rectangle,
            # the second and third value is the width and height of the Rectange but changing them has no effect on the output figure
            # alpha value controls the saturation, by default it is 1 and ranges can be passed from 0-1
        else:
            ax.add_patch(patches.Rectangle((i, 0), 1, 1, color=colour))
    
    plt.xlim(0, len(colours))
    plt.axis('off')
    plt.show()
