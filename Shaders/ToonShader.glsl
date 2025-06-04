#version 330 core

layout(location = 0) in vec3 aPos;

layout(location = 1) in vec2 aTexCoord;

out vec2 TexCoord;

void main()
{
    gl_Position = vec4(aPos, 1.0);

    TexCoord = aTexCoord;
}

in vec2 TexCoord;

out vec4 FragColor;

uniform sampler2D ourTexture;

uniform vec3 lightColor;

uniform vec3 lightPos;

uniform vec3 viewPos;

void main()
{
    vec3 texColor = texture(ourTexture, TexCoord).rgb;

    vec3 norm = normalize(vec3(0.0, 0.0, 1.0));

    vec3 lightDir = normalize(lightPos - vec3(gl_FragCoord.xy, 0.0));

    float diff = max(dot(norm, lightDir), 0.0);

    if(diff > 0.5)
    {
        diff = 1.0;
    }

    else if(diff > 0.2)
    {
        diff = 0.7;
    }

    else
    {
        diff = 0.3;
    }

    vec3 result = diff * texColor * lightColor;

    FragColor = vec4(result, 1.0);
}