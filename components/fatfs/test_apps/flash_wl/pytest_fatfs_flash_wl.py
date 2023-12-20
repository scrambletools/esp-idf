# SPDX-FileCopyrightText: 2022-2024 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0
import pytest
from pytest_embedded import Dut


@pytest.mark.esp32
@pytest.mark.esp32c3
@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        'default',
        'release',
        'fastseek',
        'no_dyn_buffers',
    ]
)
def test_fatfs_flash_wl_generic(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    dut.write('')
    dut.expect_exact('Enter test for running.')
    dut.write('*')
    dut.expect_unity_test_output(timeout=180)


@pytest.mark.esp32
@pytest.mark.generic
@pytest.mark.psram
@pytest.mark.parametrize(
    'config',
    [
        'psram',
    ]
)
def test_fatfs_flash_wl_psram(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    dut.write('')
    dut.expect_exact('Enter test for running.')
    dut.write('*')
    dut.expect_unity_test_output(timeout=180)
