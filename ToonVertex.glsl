#version 330 core

layout(location = 0) in vec3 position;

layout(location = 1) in vec3 normal;

out vec3 fragNormal;

out vec3 fragPosition;

uniform mat4 model;

uniform mat4 view;

uniform mat4 projection;

void main()
{
    fragPosition = vec3(model * vec4(position, 1.0));

    fragNormal = mat3(transpose(inverse(model))) * normal;

    gl_Position = projection * view * vec4(fragPosition, 1.0);
}