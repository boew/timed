(defun boepp2 ()
       ""
       (interactive)
       (goto-char (point-min))
       (while (search-forward-regexp "\n\\([^ai]\\)" nil t)
       	 (replace-match "\t\\1"))
)

(defun boepp ()
       ""
       (interactive)

       (setq dateLine "^==.+==$")
       (goto-char (point-min))
       (delete-matching-lines dateLine)
       
       (setq siteLine "^https://[^.]+\.\\(.*\\)\.com/$"
       	     siteLineReplace "\\1")
       (goto-char (point-min))
       (while (search-forward-regexp siteLine nil t)
       	 (replace-match siteLineReplace))
       
       (setq clockN "[ [:digit:].]+"
       	     clockLine (format "Total wall clock time:\\(%sm\\)?\\(%ss\\)?"
       			       clockN clockN)
       	     clockLineReplace "\\1\t\\2")
       (goto-char (point-min))
       (while (search-forward-regexp clockLine nil t)
       	 (replace-match clockLineReplace))
       
       (setq year "[[:digit:]]\\{4\\}"
	     month "[[:digit:]]\\{2\\}"
	     day "[[:digit:]]\\{2\\}"
	     hour "[[:digit:]]\\{2\\}"
	     minute "[[:digit:]]\\{2\\}"
	     second "[[:digit:]]\\{2\\}"
	     fLine (format "^FINISHED --\\(%s\\)-\\(%s\\)-\\(%s\\) \\(%s\\):\\(%s\\):\\(%s\\)--$"
			   year month day hour minute second)
	     fLineReplace "\\1\t\\2\t\\3\t\\4\t\\5\t\\6"
	     )
       (goto-char (point-min))
       (while (search-forward-regexp fLine nil t)
	 (replace-match fLineReplace))

       (setq nFiles "[[:digit:]]+"
	     nMB "[[:digit:].]+M"
	     nSec "[[:digit:].]+s"
	     nMbs "[[:digit:].]+"
	     dlLine (format "Downloaded: \\(%s\\) files, \\(%s\\) in \\(%s\\) (\\(%s\\) Mb/s)"
			    nFiles nMB nSec  nMbs)
	     dlLineReplace "\\1\t\\2\t\\3\t\\4"
	     )
       (goto-char (point-min))
       (while (search-forward-regexp dlLine nil t)
	 (replace-match dlLineReplace))
       )


(defun not-used () "" 
; Downloaded: 68 files, 4.6M in 1.1s (34.4 Mb/s)
       )

(defun old2boepp ()
       ""
       (interactive)

       (setq dateLine "^==.+==$")
       (goto-char (point-min))
       (delete-matching-lines dateLine)
       
       (setq siteLine "^https://[^.]+\.\\(.*\\)\.com/$"
	     siteLineReplace "\\1")
       (goto-char (point-min))
       (while (search-forward-regexp siteLine)
	 (replace-match siteLineReplace))
       
       (setq clockN "[ [:digit:].]+"
	     clockLine (format "Total wall clock time:\\(%sm\\)?\\(%ss\\)?"
			       clockN clockN)
	     clockLineReplace "\\1\t\\2")
       (goto-char (point-min))
       (while (search-forward-regexp clockLine)
	 (replace-match clockLineReplace))
       
       (setq year "[[:digit:]]\\{4\\}"
	     month "[[:digit:]]\\{2\\}"
	     day "[[:digit:]]\\{2\\}"
	     hour "[[:digit:]]\\{2\\}"
	     minute "[[:digit:]]\\{2\\}"
	     second "[[:digit:]]\\{2\\}"
	     fLine (format "^FINISHED --\\(%s\\)-\\(%s\\)-\\(%s\\) \\(%s\\):\\(%s\\):\\(%s\\)--$"
			   year month day hour minute second)
	     fLineReplace "\\1\t\\2\t\\3\t\\4\t\\5\t\\6\t"
	     )
       (goto-char (point-min))
       (while (search-forward-regexp fLine)
	 (replace-match fLineReplace))
       )

(defun old1boepp ()
       ""
       (interactive)
       (setq l2 "==\nhttps://blog.adafruit.com/")
       (setq l2q (regexp-quote l2))
       (search-forward l2)
       (forward-line -1)
       (search-forward-regexp "\n\\([^=]\\)")
       (replace-match "\t\\1")
       (insert "HERENOW")
       )
