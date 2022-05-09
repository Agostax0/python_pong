import turtle;

def create_paddle():
    paddle = turtle.Turtle()    
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.score = 0
    return paddle
def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")  
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 1
    ball.dy = 1
    return ball
def create_scoreboard():
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.penup()
    score_board.color("white")
    score_board.hideturtle()
    score_board.goto(0,240)
    score_board.write("Player A: 0\t Player B: 0",align="center",font=("Courier",24,"normal"))
    return score_board
def paddle_a_move_up():
    paddle_a.sety(paddle_a.ycor()+10)
def paddle_a_move_down():
    paddle_a.sety(paddle_a.ycor()-10)
def paddle_b_move_up():
    paddle_b.sety(paddle_b.ycor()+10)
def paddle_b_move_down():
    paddle_b.sety(paddle_b.ycor()-10)

def listen():
    window.listen()
    window.onkeypress(paddle_a_move_up,"w")  
    window.onkeypress(paddle_a_move_down,"s")  
    window.onkeypress(paddle_b_move_up,"Up")  
    window.onkeypress(paddle_b_move_down,"Down") 
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)  
 
def border_check():
    if ball.ycor() > 295:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -285:
        ball.sety(-280)
        ball.dy *= -1
    if ball.xcor() > 385:
        #score for a
        paddle_a.score += 1
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -395:
        #score for b
        paddle_b.score += 1
        ball.goto(0,0)
        ball.dx *= -1
def paddle_check():
    if (ball.xcor() < paddle_a.xcor() + 20):
        if(ball.ycor() > paddle_a.ycor() - 50 and ball.ycor() < paddle_a.ycor() + 50):
            ball.dx *= -1;
    if (ball.xcor() > paddle_b.xcor() - 20):
        if(ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50):
            ball.dx *= -1;
def update_score_board():
    score_board.clear()
    score_board.write("Player A: {}\t Player B: {}".format(paddle_a.score,paddle_b.score),align="center",font=("Courier",24,"normal"))
  
window = turtle.Screen()

window.bgcolor("black")

window.setup(width=800, height=600)

window.tracer(0)
paddle_a = create_paddle()
paddle_b = create_paddle()
ball = create_ball()
score_board = create_scoreboard()
paddle_a.goto(-350,0)
paddle_b.goto(350,0)



while True:
    listen()
    window.update()
    move_ball()
    border_check()
    paddle_check()
    update_score_board()
    
    
    
    
    








