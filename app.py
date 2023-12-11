from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 댓글 데이터를 저장할 간단한 리스트
comments = []


@app.route('/')
def index():
    return render_template('index.html', comments=comments)


@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form.get('name')
    content = request.form.get('content')
    
    if name and content:
        new_comment = {'name': name, 'content': content, 'likes': 0, 'replies': []}
        comments.append(new_comment)
    
    return redirect(url_for('index'))


@app.route('/like_comment/<int:comment_index>', methods=['POST'])
def like_comment(comment_index):
    comments[comment_index]['likes'] += 1
    return redirect(url_for('index'))


@app.route('/add_reply/<int:comment_index>', methods=['POST'])
def add_reply(comment_index):
    content = request.form.get('reply_content')
    
    if content:
        new_reply = {'name': 'Anonymous', 'content': content}
        comments[comment_index]['replies'].append(new_reply)
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
