# rpm_device is the name of the ported device
%define rpm_device condor
# rpm_vendor is used in the rpm space
%define rpm_vendor motorola
# Manufacturer and device name to be shown in UI
%define vendor_pretty Motorola
%define device_pretty Moto E
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc

