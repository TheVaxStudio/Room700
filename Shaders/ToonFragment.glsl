#version 330 core

in vec3 fragNormal;

in vec3 fragPosition;

out vec4 FragColor;

uniform vec3 lightPos;

uniform vec3 viewPos;

uniform vec3 lightColor;

uniform vec3 objectColor;

void main()
{
    vec3 norm = normalize(fragNormal);

    vec3 lightDir = normalize(lightPos - fragPosition);

    float diff = max(dot(norm, lightDir), 0.0);

    float levels = 4.0;

    diff = floor(diff * levels) / levels;

    vec3 result = diff * lightColor * objectColor;

    FragColor = vec4(result, 1.0);
}