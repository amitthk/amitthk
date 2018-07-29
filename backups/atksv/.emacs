
;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(cua-mode t nil (cua-base))
 '(custom-enabled-themes (quote (tango-dark)))
 '(ido-mode (quote both) nil (ido))
 '(org-default-priority 67)
 '(org-lowest-priority 73)
 '(package-archives
   (quote
    (("gnu" . "http://elpa.gnu.org/packages/")
     ("melpa" . "https://melpa.org/packages/"))))
 '(package-selected-packages
   (quote
    (magit auto-complete org-dropbox notes-mode nlinum org))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "Courier New" :foundry "outline" :slant normal :weight normal :height 143 :width normal)))))
 
(cua-mode t)
(global-visual-line-mode t)
(setq org-directory "/home/pi/Documents/src/atksv")
(setq org-default-notes-file (concat org-directory "/captures.org"))
(define-key global-map "\C-cc" 'org-capture)
(setq org-agenda-files
      '("inbox.org" "actionable.org" "references.org" "someday.org" "done.org" "higheraltitudes.org"))
(setq org-refile-targets
      '((nil :maxlevel . 3)
        (org-agenda-files :maxlevel . 3)))
