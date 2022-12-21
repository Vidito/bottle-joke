% rebase('base.tpl', title = 'Jokes')

    <h1>Random Software Joke</h1>
    % import datetime
    <p> {{ datetime.datetime.now().strftime("%c") }} </p>
    <p> {{ joke }} </p>

