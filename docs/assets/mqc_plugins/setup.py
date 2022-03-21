#!/usr/bin/env python

from setuptools import setup, find_packages


_version = '0.0.1'

setup(
    name='multiqc_custom_plugins',
    version=_version,
    description="Custom MultiQC plugins for RRBS pipeline",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['multiqc==1.9'],
    entry_points={
        'multiqc.templates.v1': [
            'zymo = plugins.templates.zymo'
        ],
        'multiqc.modules.v1': [
            'fastqc = plugins.modules.fastqc_ext:MultiqcModule',
            'cutadapt = plugins.modules.cutadapt_ext:MultiqcModule',
            'bismark = plugins.modules.bismark_ext:MultiqcModule',
            'samtools = plugins.modules.samtools_ext:MultiqcModule',
            'methyldackel = plugins.modules.methyldackel:MultiqcModule',
            'correlation = plugins.modules.correlation:MultiqcModule',
            'download = plugins.modules.download:MultiqcModule',
        ],
        'multiqc.hooks.v1': [
            'before_config = plugins.utils.hooks:before_config',
            'execution_start = plugins.utils.hooks:execution_start',
            'after_modules = plugins.utils.hooks:after_modules'
        ],
    }
)
