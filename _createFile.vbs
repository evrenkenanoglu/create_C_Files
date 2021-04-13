Set objFSO = CreateObject( "Scripting.FileSystemObject" )

' Enter parameters
fileName = inputbox( "What is the name of the file?" & vbCrLf & "example: camel_Case" )
if fileName = "" then
msgbox "ERROR: EMPTY FILE NAME"
wscript.quit
end if
if len(fileName) < 3 then
msgbox "ERROR: SHORT FILE NAME"
wscript.quit
end if
briefDesc = inputbox( "What is it about?" )
author = inputbox( "Who is the author?" )


' Create C file
Set objFile = objFSO.OpenTextFile( "_createFile_c", 1 )
template = ""
Do Until objFile.AtEndOfStream
    template = template & objFile.ReadLine & vbCrLf
Loop
objFile.Close

template = replace( template, "%FILENAMELC%", lcase( fileName ) )
template = replace( template, "%FILENAMEUC%", ucase( fileName ) )
template = replace( template, "%FILENAMEPC%", ucase( left(fileName,1) ) & lcase( right(fileName, len(fileName) - 1 ) ) )
template = replace( template, "%AUTHOR%", author )
template = replace( template, "%BRIEF%", briefDesc )
template = replace( template, "%YEAR%", year(now) )
template = replace( template, "%DATE%", formatdatetime( now, vbShortDate ) )

Set objFile = objFSO.CreateTextFile( lcase( fileName ) & ".c", True )
objFile.Write template
objFile.Close


' Create H file
Set objFile = objFSO.OpenTextFile( "_createFile_h", 1 )
template = ""
Do Until objFile.AtEndOfStream
    template = template & objFile.ReadLine & vbCrLf
Loop
objFile.Close

template = replace( template, "%FILENAMELC%", lcase( fileName ) )
template = replace( template, "%FILENAMEUC%", ucase( fileName ) )
template = replace( template, "%FILENAMEPC%", ucase( left(fileName,1) ) & lcase( right(fileName, len(fileName) - 1 ) ) )
template = replace( template, "%AUTHOR%", author )
template = replace( template, "%BRIEF%", briefDesc )
template = replace( template, "%YEAR%", year(now) )
template = replace( template, "%DATE%", formatdatetime( now, vbShortDate ) )

Set objFile = objFSO.CreateTextFile( lcase( fileName ) & ".h", True )
objFile.Write template
objFile.Close
