function changeLang(langCode) {
    document.documentElement.setAttribute("lang", langCode);
    location.hash = langCode;
    // location.reload();
    fetch("{{ url_for('static', filename='test.json') }}", {
        headers : { 
          'Content-Type': 'application/json',
          'Accept': 'application/json'
         }
      }).then((res) => {
        return res.json();
      })
      .then((data) => document.getElementById("Text").innerHTML = 
            (data.users[0].site + " - " + data.users[0].user));
}