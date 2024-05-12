from manim import *

class HTTPRequest(Scene):
    def construct(self):
        space = 2

        client_square = Square(color=BLUE, fill_opacity=0.5).shift(LEFT*2)
        client_square.shift(LEFT * space)
        client_text = Text("Client").move_to(client_square.get_center())

        api_square = Square(color=RED, fill_opacity=0.5).shift(RIGHT*2)
        api_square.shift(RIGHT * space)
        api_text = Text("API").move_to(api_square.get_center())

        arrow_request = Arrow(client_square.get_right(), api_square.get_left()).shift(DOWN * 0.1)
        request_text = Text("Requisição").move_to(arrow_request.get_center() + UP * 0.5)
        arrow_response = Arrow(api_square.get_left(), client_square.get_right()).shift(DOWN * 0.1)
        response_text = Text("Resposta").move_to(arrow_response.get_center() + UP * 0.5)

        self.add(client_square, api_square, client_text, api_text)
        self.wait(1)
        self.play(FadeIn(arrow_request, request_text))
        self.play(FadeOut(arrow_request), FadeOut(request_text))
        self.play(FadeIn(arrow_response, response_text))
        self.play(FadeOut(arrow_response), FadeOut(response_text))
