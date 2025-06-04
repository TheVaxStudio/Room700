import OpenGL.GL as gl

class ToonShader:
    def __init__(self, vertex_shader_source, fragment_shader_source):
        self.shader_program = self.compile_shader(vertex_shader_source, fragment_shader_source)

    def compile_shader(self, vertex_src, fragment_src):
        vertex_src = '../Shaders/ToonVertex.glsl'
        fragment_src = '../Shaders/ToonFragment.glsl'

    def use(self):
        gl.glUseProgram(self.shader_program)

    def set_uniform_float(self, name, value):
        location = gl.glGetUniformLocation(self.shader_program, name)
        gl.glUniform1f(location, value)

    def set_uniform_vec3(self, name, value):
        location = gl.glGetUniformLocation(self.shader_program, name)
        gl.glUniform3f(location, *value)

    def set_toon_threshold(self, threshold):
        location = gl.glGetUniformLocation(self.shader_program, "toonThreshold")
        gl.glUniform1f(location, threshold)

    def set_outline_color(self, color):
        location = gl.glGetUniformLocation(self.shader_program, "outlineColor")
        gl.glUniform3f(location, *color)