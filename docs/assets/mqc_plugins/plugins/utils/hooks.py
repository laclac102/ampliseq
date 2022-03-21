#!/usr/bin/env python
import logging

from multiqc import config
from multiqc.utils import report

log = logging.getLogger('multiqc')


def before_config():
    # Use the zymo template by default
    log.info('Load MultiQC report template: zymo')
    config.template = 'zymo'


def execution_start():
    log.info("Load custom plugin search patterns")
    search_patterns = {
        'methyldackel': {
            'fn': '*_methyldackel.txt'
        },
        'correlation': {
            'fn': '*_correlation.txt'
        },
        'download': {
            'fn': '*_download.txt'
        }
    }
    fn_clean_exts = [
        '_methyldackel',
        '_correlation',
        '_download',
    ]
    config.fn_clean_exts.extend(fn_clean_exts)
    config.update_dict(config.sp, search_patterns)
    return


def after_modules():
    """Plugin code to run when MultiQC modules have completed."""
    for mod in report.modules_output:
        # Hide subsection header of Picard: Insert Size
        if mod.__class__.__module__.find("picard") != -1:
            log.info("Change picard subsection title")
            mod.sections[0]['name'] = ""
            mod.sections[0]['description'] = "<p></p>"
    return
