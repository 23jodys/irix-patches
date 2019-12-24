product patchXX00001
    id "User Patch 00001, update system sh to mksh"
    image eoe
        id "Basic IRIX updates (sh)"
        version 2
        order 9999
        subsys man 
            patch
            id "mksh man pages"
            follows eoe.man.base 1289434520 1289434520
            exp patchXX00001.eoe.man
        endsubsys
        subsys sw 
            patch
            id "mksh binaries"
            follows eoe.sw.base 1289434520 1289434520
            exp patchXX00001.eoe.sw
        endsubsys
    endimage
endproduct
