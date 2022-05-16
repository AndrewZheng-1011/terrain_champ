#ifndef QUADRUPED_DESCRIPTION_H
#define QUADRUPED_DESCRIPTION_H

#include <quadruped_base/quadruped_base.h>

namespace champ
{
    namespace URDF
    {
        void loadFromHeader(champ::QuadrupedBase &base)
        {
      base.lf.hip.setOrigin(0.0705, 0.04, 0.02425, 0.0, 0.0, 0.0);
base.lf.upper_leg.setOrigin(0.02735, 0.029523, -0.0012724, 0.11522, 0.436332, 0.1069);
base.lf.lower_leg.setOrigin(0.022028, 0.0023333, -0.12152, -3.1416, -2.35619, 3.1416);
     base.lf.foot.setOrigin(-0.01, 0.0, -0.116, 0.0, 0.0, 0.0);

      base.rf.hip.setOrigin(0.0705, -0.04, 0.02425, 0.0, 0.0, 0.0);
base.rf.upper_leg.setOrigin(0.02735, -0.029523, -0.0012724, -0.11522, 0.436332, -0.1069);
base.rf.lower_leg.setOrigin(0.022028, -0.0023333, -0.12152, 3.1416, -2.35619, -3.1416);
     base.rf.foot.setOrigin(-0.01, 0.0, -0.116, 0.0, 0.0, 0.0);

      base.lh.hip.setOrigin(-0.1299, 0.04, 0.02425, 0.0, 0.0, 0.0);
base.lh.upper_leg.setOrigin(0.02775, 0.029523, -0.0012724, 0.11522, 0.436332, 0.1069);
base.lh.lower_leg.setOrigin(0.022028, 0.0026233, -0.12152, -3.1416, -2.35619, 3.1416);
     base.lh.foot.setOrigin(-0.01, 0.0, -0.116, 0.0, 0.0, 0.0);

      base.rh.hip.setOrigin(-0.0705, -0.04, 0.02425, 0.0, 0.0, 0.0);
base.rh.upper_leg.setOrigin(-0.17265, -0.029523, -0.0012724, -0.11522, 0.436332, -0.1069);
base.rh.lower_leg.setOrigin(0.022028, -0.0025833, -0.12152, 3.1416, -2.35619, -3.1416);
     base.rh.foot.setOrigin(-0.01, 0.0, -0.116, 0.0, 0.0, 0.0);
        }
    }
}
#endif