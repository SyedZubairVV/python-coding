def timeConversion(s):
    # Write your code here

    if s[8] == "A":
        if s[:2] == "12":
            sbew = s.replace(s[:2], "00")
            return(sbew[:8])
        else:
            return(s[:8])
    else:
        if s[:2] == "12":
            return(s[:8])
        else:
            hour = int(s[:2])
            hour = hour + 12
            snew = s.replace(s[:2], str(hour))
            spew = snew.replace(s[8:10], "")
            return(spew)
