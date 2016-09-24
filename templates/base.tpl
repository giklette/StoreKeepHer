<html>
<head>
    <title>{{title}}</title>
    <link href='static/style.css' rel='stylesheet' type='text/css'>
</head>

<body>
    % include('templates/header.tpl')
    {{!base}}
    % include('templates/footer.tpl', content='this is the footer from base.tpl')
</body>
</html>